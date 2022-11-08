def notas(*n,sit=False):
    """
    gsogbodf
    :param n: khasgkh
    :param sit: hkgkh
    :return: jdsnghjohbj
    """
    from statistics import mean
    resp={}
    resp['total']=sum(n)
    resp['maior']=max(n)
    resp['menor']=min(n)
    resp['media']=mean(n)
    if sit==True:
        if resp['media']>7:
           resp['situação']='Muito bom'
        if resp['media']<5:
            resp['situação']='Muito ruim'
        else:
            resp['situação']='Razoavel'
    return resp

resp= notas(5.5,2.5,10,sit=True)
print(resp)