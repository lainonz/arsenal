import os
from os.path import dirname, abspath, expanduser, join

# Save original working directory where user launched arsenal
# ARSENAL_LAUNCH_DIR is set by the 'run' script before cd to arsenal directory
# This preserves the user's actual working directory for file operations
ORIGINAL_CWD = os.environ.get('ARSENAL_LAUNCH_DIR', os.getcwd())

# Base paths
DATAPATH = join(dirname(dirname(abspath(__file__))), 'data')
BASEPATH = dirname(dirname(dirname(abspath(__file__))))
HOMEPATH = expanduser("~")
FORMATS = ["md", "rst", "yml"]
EXCLUDE_LIST = ["README.md", "README.rst", "index.rst"]
FUZZING_DIRS = ["/usr/local/share/wordlists/**/*.txt"]

CHEATS_PATHS = [
    # join(DATAPATH, "cheats"),  # DEFAULT
    # Additional paths below, add comma to line above
    # join(BASEPATH, "my_cheats"),
    join(HOMEPATH, ".cheats"),
]

messages_error_missing_arguments = 'Error missing arguments'

# set lower delay to use ESC key (in ms)
os.environ.setdefault('ESCDELAY', '25')
os.environ['TERM'] = 'xterm-256color'

if os.environ.get('ARSENAL_LOCAL'):
    savevarfile = join(os.getcwd(), ".arsenal.json")
else:
    savevarfile = join(HOMEPATH, ".arsenal.json")

PREFIX_GLOBALVAR_NAME = "arsenal_prefix_cmd"
