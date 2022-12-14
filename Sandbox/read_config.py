import configparser

config = configparser.ConfigParser()
print(config.sections())

config.read('config.ini')

print('User => ', config['bitbucket.org']['User'])
print('ForwardX11 => ', config['bitbucket.org']['ForwardX11'])

print(config.sections())

print('bitbucket.org' in config)

print('bytebong.com' in config)

print(config['bitbucket.org']['User'])

print(config['DEFAULT']['Compression'])

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])

print(topsecret['Port'])

for key in config['bitbucket.org']:
    print(key)





config['bitbucket.org']['ForwardX11']