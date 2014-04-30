#!/usr/bin/env python2

# Copy this file to config.py, then amend the settings below according to
# your system configuration.

# Override the path to the Android SDK, $ANDROID_HOME by default
sdk_path = "android-sdk-linux"

# Override the path to the Android NDK, $ANDROID_NDK by default
#ndk_path = "/path/to/android-ndk"
# Build tools version to be used
build_tools = "19.0.2"

# Command for running Ant
#ant = "/path/to/ant"
ant = "ant"

# Command for running maven 3
#mvn3 = "/path/to/mvn"
mvn3 = "mvn"

# Command for running Gradle
#gradle = "/path/to/gradle"
gradle = "gradle"

# Set the maximum age (in days) of an index that a client should accept from
# this repo. Setting it to 0 or not setting it at all disables this
# functionality. If you do set this to a non-zero value, you need to ensure
# that your index is updated much more frequently than the specified interval.
# The same policy is applied to the archive repo, if there is one.
repo_maxage = 0

repo_url = "http://fwhost.github.io/fdr/repo"
repo_name = "F-Droid-U"
repo_icon = "fdroid-icon.png"
repo_description = """
Repo for F-Droid U.
"""

# As above, but for the archive repo.
# archive_older sets the number of versions kept in the main repo, with all
# older ones going to the archive. Set it to 0, and there will be no archive
# repository, and no need to define the other archive_ values.
archive_older = 0
archive_url = "https://f-droid.org/archive"
archive_name = "F-Droid Archive"
archive_icon = "fdroid-icon.png"
archive_description = """
The archive repository of the F-Droid client. This contains older versions
of applications from the main repository.
"""


#The key (from the keystore defined below) to be used for signing the
#repository itself. Can be None for an unsigned repository.
repo_keyalias = "fdrepokey"

#The keystore to use for release keys when building. This needs to be
#somewhere safe and secure, and backed up!
keystore = "al.keystore"

# The password for the keystore (at least 6 characters).  If this password is
# different than the keypass below, it can be OK to store the password in this
# file for real use.  But in general, sensitive passwords should not be stored
# in text files!
keystorepass = ""

# The password for keys - the same is used for each auto-generated key as well
# as for the repository key.  You should not normally store this password in a
# file since it is a sensitive password.
keypass = ""

#The distinguished name used for all keys.
keydname = "CN=Birdman, OU=Cell, O=Alcatraz, L=Alcatraz, S=California, C=US"

#Use this to override the auto-generated key aliases with specific ones
#for particular applications. Normally, just leave it empty.
keyaliases = {}
keyaliases['com.example.app'] = 'example'
#You can also force an app to use the same key alias as another one, using
#the @ prefix.
keyaliases['com.example.another.plugin'] = '@com.example.another'

# The full path to the root of the repository.  It must be specified in
# rsync/ssh format for a remote host/path. This is used for syncing a locally
# generated repo to the server that is it hosted on.  It must end in the
# standard public repo name of "/fdroid", but can be in up to three levels of
# sub-directories (i.e. /var/www/packagerepos/fdroid).
serverwebroot = ''

# If you want to force 'fdroid server' to use a non-standard serverwebroot
#nonstandardwebroot = True

#Wiki details
wiki_protocol = "http"
wiki_server = "server"
wiki_path = "/wiki/"
wiki_user = "login"
wiki_password = "1234"

#Only set this to true when running a repository where you want to generate
#stats, and only then on the master build servers, not a development
#machine.
update_stats = False

#Use the following to push stats to a Carbon instance:
stats_to_carbon = False
carbon_host = '0.0.0.0'
carbon_port = 2003

#Set this to true to always use a build server. This saves specifying the
#--server option on dedicated secure build server hosts.
build_server_always = False

# Limit in number of characters that fields can take up
# Only the fields listed here are supported, defaults shown
char_limits = {
    'Summary' : 50,
    'Description' : 1500
}
