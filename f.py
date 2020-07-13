import requests,bs4,sys,os,datetime


#print(len(sys.argv))

if len(sys.argv)==1:
    res = requests.get('https://www.worldometers.info/coronavirus/')
else:
    res = requests.get('https://www.worldometers.info/coronavirus/country/'+sys.argv[1])

if len(res.text)==1836:
    raise ValueError('Enter a valid country name')


 
sp = bs4.BeautifulSoup(res.content,'html.parser')

r = sp.find_all('div',id='maincounter-wrap')

w =[0,0,0]
for i in range(3):
    w[i]=int(r[i].find('span').get_text().strip().replace(',',''))


print('Total Cases: {}\nTotal Deaths: {}\nTotal Recovered: {}\n'.format(w[0],w[1],w[2]))


area = 'world'
if len(sys.argv)!=1:
    area = sys.argv[1]

path = area + '.txt'
if os.path.exists(path):
    l=[]
    f = open(path,'r')
    r=f.readlines()
    f.close()
    for i in r:
        l.append(i.strip())

    print('Last checked: '+l[3])
    print('Change in\nCases: +{}\nDeaths: +{}\nRecovered: +{}\n'.format(w[0]-int(l[0]),w[1]-int(l[1]),w[2]-int(l[2])))    


tm = datetime.datetime.now()
tm = tm.strftime("%b %d %Y %H:%M:%S")
f = open(path,'w')
for i in w:
    f.write('%d\n'%i)
f.write('%s\n'%tm)
f.close()


    
