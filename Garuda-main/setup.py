import pickle
import pyfiglet
import os
print(pyfiglet.Figlet(font='slant').renderText('Garuda'))
print('\nChoose an option')
print('[1] Enter Shodan API key')
print('[2] Enter Geolocation.io API key')
choice = int(input('[~] Enter choice :: '))
if choice == 1:
    api = str(input('[~] Enter API key: '))
    if os.name == 'nt':
        s_file = 'core\\shodan.dat'
    else:
        s_file = 'core/shodan.dat'
    with open(s_file, 'wb') as f:
        pickle.dump([api], f)
    f.close()
    input('[i] Saved in core/shodan.dat. Press enter to exit...')
    exit()
else:
    gapi = str(input('Enter API key: '))
    if os.name == 'nt':
        g_file = 'core\\geolocation.dat'
    else:
        g_file = 'core/geolocation.dat'
    with open(g_file, 'wb') as f:
            pickle.dump([gapi], f)
    f.close()
    input('Saved in core/geolocation.dat. Press enter to exit...')
    exit()
