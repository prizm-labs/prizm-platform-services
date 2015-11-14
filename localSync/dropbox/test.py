# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 's18vv906j28753i'
app_secret = 'pnoyg0doihxkt4y'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
# authorize_url = flow.start()
# print '1. Go to: ' + authorize_url
# print '2. Click "Allow" (you might have to log in first)'
# print '3. Copy the authorization code.'
# code = raw_input("Enter the authorization code here: ").strip()
#
# # This will fail if the user enters an invalid authorization code
# # code = 'OT7j2mLi0RAAAAAAAAASVfBvyd8VF9oHY-GJyVQ-N9w'
# access_token, user_id = flow.finish(code)

access_token = 'OT7j2mLi0RAAAAAAAAASWB9YSIhukmap5nsX7cCl2q_O74bZ-CpUjVz6eQfv5Y2H'
client = dropbox.client.DropboxClient(access_token)
# print 'linked account: ', client.account_info()
# print access_token

f = open('working-draft.txt', 'rb')
response = client.put_file('/magnum-opus.txt', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.txt', 'wb')
out.write(f.read())
out.close()
print metadata
