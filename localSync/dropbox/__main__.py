import dropbox

import os
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

access_token = 'OT7j2mLi0RAAAAAAAAASWB9YSIhukmap5nsX7cCl2q_O74bZ-CpUjVz6eQfv5Y2H'
client = dropbox.client.DropboxClient(access_token)

print 'linked account: ', client.account_info()

# out = open('magnum-opus.txt', 'wb')
# with client.get_file('/magnum-opus.txt') as f:
#     out.write(f.read())

local_cache_path = 'apps'

root_path = 'BUILDS'
apps_path = '_Apps'
server_path = '_Server'
tabletop_path = 'Tabletop'

app_manifest = [
    { 'name':'Test', 'version':'0.0.1', 'multiscreen':False },
    { 'name':'Battle', 'version':'0.0.1', 'multiscreen':False },
    { 'name':'Capture', 'version':'0.0.1', 'multiscreen':False },
    { 'name':'Lights', 'version':'0.0.1', 'multiscreen':False },
    { 'name':'Monopoly', 'version':'0.0.1', 'multiscreen':False },
    { 'name':'Plants', 'version':'0.0.1', 'multiscreen':False },
    { 'name':'Poker', 'version':'0.0.1', 'multiscreen':True },
    { 'name':'Story', 'version':'0.0.1', 'multiscreen':False },
    { 'name':'TabletopSimulator', 'version':'0.0.1', 'multiscreen':False }
]

platform = 'windowsx64'
path_delimiter = '/'

chunk_size = 100000

for entry in app_manifest:
    package_name = entry['name']
    version_number = entry['version']
    bundle = platform+'.zip'
    full_path = ''

    if entry['multiscreen']:
        full_path = [ root_path, apps_path, package_name, tabletop_path, version_number, bundle ]
    else:
        full_path = [ root_path, apps_path, package_name, version_number, bundle ]


    full_path_str = path_delimiter.join(full_path)

    print full_path_str

    local_path = [ local_cache_path, package_name, bundle ]
    local_path_str = path_delimiter.join(local_path)

    print local_path_str

    make_sure_path_exists(local_cache_path+path_delimiter+package_name)

    # metadata = client.metadata(full_path_str)
    # print metadata

    f, metadata = client.get_file_and_metadata(full_path_str)
    print metadata

    # out = open(local_path_str, 'wb')
    # out.write(f.read())
    # out.close()

    progress = 0
    file_size = metadata[u'bytes']

    print 'starting download: '+metadata[u'size']+' ('+str(file_size)+')'

    out = open(local_path_str, 'wb')

    while True:
        chunk = f.read(chunk_size)
        out.write(chunk)
        progress = progress + len(chunk)
        progressPercent = (1.0*progress)/file_size
        print progressPercent

        if len(chunk) < chunk_size:
            out.write(chunk)
            progress = progress + len(chunk)
            progressPercent = (1.0*progress)/file_size
            print progressPercent
            break

    # chunk = f.read(chunk_size)
    # while chunk != "":
    #     # Do stuff with byte.
    #     chunk = f.read(chunk_size)
    #     out.write(chunk)
    #     progress = progress + len(chunk)
    #     progressPercent = (1.0*progress)/file_size
    #     print progressPercent


    # for line in f.readlines():
    #     print line
    #     out.write(line)


    out.close()

    print 'finished download'


# web app reads local app manifest
# diff to find new versions of apps
# assemble list of apps@version number to download
#
# called from web app
# manager.sync(manifest)
# [ appName, versionNumber or "latest" ]
#
# get OS platform
# generate list of file paths to zipped executable for platform
#
# get app cache location
# download zipped executables to app cache
# unzip bundle
# set permissions for exectuable
# update local app manifest
