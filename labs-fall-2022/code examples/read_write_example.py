
f = open('/Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/code examples/test.txt','w')
f.write('Hello, ')
f.write('world!')
f.close()

f = open('/Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/code examples/test.txt','a')
f.write('Hello, ')
f.write('world!')
f.close()

f = open('/Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/code examples/test.txt','r+')
f.write('Hello, ')
f.write('worldstuff!')
f.close()
