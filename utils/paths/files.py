"""
The files module: Provides path to all necessary files.

This module helps with the relative paths of the files in this package.
Similar to `directories.py` module it helps with overcoming the hassle
of re-writing and hardcoding paths used for reference.

The structure of the module is following:
 - ai_file{}:           Dictionary of all the important files used in
                        the package.

See https://github.com/xames3/charlotte for cloning the repository.
"""
#   History:
#
#   < Checkout my github repo for history and latest stable build >
#
#   1.1.1 - Made the code more* PEP-8 compliant.
#   1.0.3 - Added reference link to ngrok file.
#   1.0.0 - First code.

from charlotte.utils.paths.directories import PARENT, ai_dir

ai_file = {
    'init': '__init__.py',
    'nlu': ai_dir['data']/'nlu.md',
    'actions': PARENT/'actions.py',
    'config': PARENT/'config.yml',
    'domain': PARENT/'domain.yml',
    'endpoints': PARENT/'endpoints.yml',
    'music': ai_dir['csv']/'music.csv',
}
