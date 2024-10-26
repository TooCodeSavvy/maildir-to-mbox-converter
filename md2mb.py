#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
Frédéric Grosshans, 19 January 2012
Nathan R. Yergler, 6 June 2010

This file does not contain sufficient creative expression to invoke
assertion of copyright. No warranty is expressed or implied; use at
your own risk.

---

Uses Python's included mailbox library to convert mail archives from
Maildir [http://en.wikipedia.org/wiki/Maildir] to 
Mbox [http://en.wikipedia.org/wiki/Mbox] format, including subfolders.

For detailed documentation on the mailbox library, refer to:
http://docs.python.org/library/mailbox.html#mailbox.Mailbox.

---

To run, save as md2mb.py and execute:

$ python md2mb.py [maildir_path] [mbox_filename]

- [maildir_path]: The path to the Maildir, which should contain the folders `new`, `cur`, and `tmp`, along with any subfolders.
- [mbox_filename]: The output Mbox file name that will be created. Additionally, a directory named [mbox_filename].sbd will be created to maintain subfolder structure.
"""

import mailbox
import sys
import email
import os

def maildir2mailbox(maildirname, mboxfilename):
    """
    Converts a Maildir to an Mbox file.
    
    Args:
        maildirname (str): Path to the Maildir directory.
        mboxfilename (str): Name of the output Mbox file.
    
    This function reads emails from the specified Maildir and writes them to 
    the specified Mbox file, preserving the email structure.
    """
    # Open the existing Maildir and the target Mbox file
    maildir = mailbox.Maildir(maildirname, email.message_from_binary_file)
    mbox = mailbox.mbox(mboxfilename)

    # Lock the Mbox to prevent concurrent writes
    mbox.lock()

    # Iterate over messages in the Maildir and add them to the Mbox
    for msg in maildir:
        mbox.add(msg)

    # Close the Mbox and Maildir
    mbox.close()
    maildir.close()

# Create the main mailbox
dirname = sys.argv[-2]  # Get the Maildir path from the command-line arguments
mboxname = sys.argv[-1]  # Get the desired Mbox filename from the command-line arguments
print(dirname + ' -> ' + mboxname)  # Print the conversion message

mboxdirname = mboxname + '.sbd'  # Create a directory name for subfolders
maildir2mailbox(dirname, mboxname)  # Convert the Maildir to Mbox

# Create the subdirectory for storing subfolders if it doesn't exist
if not os.path.exists(mboxdirname): 
    os.makedirs(mboxdirname)

# Process any subdirectories within the Maildir
listofdirs = [dn for dn in next(os.walk(dirname))[1] if dn not in ['new', 'cur', 'tmp']]
for curfold in listofdirs:
    # Create the subfolder path
    curlist = [mboxname] + curfold.split('.')
    curpath = os.path.join(*[dn + '.sbd' for dn in curlist if dn])
    
    # Create the subfolder if it doesn't exist
    if not os.path.exists(curpath): 
        os.makedirs(curpath)
    
    # Print the mapping of Maildir subfolder to Mbox subfolder
    print('| ' + curfold + ' -> ' + curpath[:-4])
    
    # Convert the subfolder
    maildir2mailbox(os.path.join(dirname, curfold), curpath[:-4])

print('Done')  # Indicate that the conversion is complete
