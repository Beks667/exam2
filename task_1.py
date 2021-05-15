def func(name,**kwargs):
    print(f'{name}')
    for elem in kwargs:
        print(f'{elem}-{kwargs[elem]}')

func(name='USA',population='330 million',is_democratic=True)
func(name='Kyrgyzstan',area ='200km2',borders=['KZ','UZ','CH'])
func(name = 'Japan',anime=True,jdm=True)