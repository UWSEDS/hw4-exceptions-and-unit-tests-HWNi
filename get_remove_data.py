import os
import urllib3

# Downloads the data if it is not present locally
# If the data are already present, then it takes no action
def get_data(url):
    
    filename = os.path.basename(url)
    http = urllib3.PoolManager()
    case = ''
    if os.path.exists(filename):
        print(filename + 'exists locally.')
        case = 'File exists'
    else:
        try:
            r = http.request('GET', url)
            with open(filename, 'wb') as f:
                f.write(r.data)
                f.close()
            print('Download succeeds.')
            case = 'No local file but URL exists'
        except:
            print('URL does not exist.')
            case = 'URL does not exist'
    return case

# Removes the data if it is present locally.
def remove_data(url):
    filename = os.path.basename(url)
    case = ''
    if os.path.exists(filename):
        os.remove(filename)
        print('"' + filename + '" deleted')
        case = 'Remove succeeds'
    else:
        print('File does not exist')
        case = 'Local file does not exist'
    return case