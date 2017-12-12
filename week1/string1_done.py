def donuts(count):
    ret="number of donuts:"
    if count<10:  ret=ret+str(count)
    else: ret=ret+"many"
    return ret
def both_ends(s):
    if len(s)<2: return ""
    return s[0:2]+s[-2:]
def fix_start(s):
    if len(s)<=1: return ""
    f=s[0]
    l=s[1:]
    return f+l.replace(f,"*")
def mix_up(a,b):
    a_new=b[0:2]+a[2:]
    b_new=a[0:2]+b[2:]
    return a_new+" "+b_new

def test(got,expected):
    if got==expected:
       print("Pass")
    else:
       print("Fail")
def main():
    test(donuts(5),"number of donuts:5")
    test(donuts(50), "number of donuts:many")
    test(donuts(50), "number of donuts:50")
    test(both_ends("mikhailgladchenko"),"miko")
    test(both_ends("mikhailgladchenko"), "komi")
    test(both_ends("m"), "")
    test(both_ends("m"), "m")
    test(fix_start("oloko"),"ol*k*")
    test(fix_start("o"), "")
    test(fix_start("donut"), "donut")

    test(mix_up("mix","pod"),"pox mid")
    test(mix_up("mix", "pod"), "pox mud")
    test(mix_up("gnash", "sport"), "spash gnort")
    test(mix_up("pezzy", "firm"), "fizzy perm")
if __name__ == '__main__':
  main()
