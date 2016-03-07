'''
pys -- pythons
'''
import re;

def conv(arg,default=None,func=None):
    '''
    essentially, the generalization of
    
    arg if arg else default

    or

    func(arg) if arg else default
    '''
    if func:
        return func(arg) if arg else default;
    else:
        return arg if arg else default;

def test(d,k):
    '''short for "k in d and d[k]'''
    return k in d and d[k];

def dump_pickle(name, obj):
    '''quick pickle dump similar to np.save'''
    with open(name,"wb") as f:
        pickle.dump(obj,f,2);
    pass;

def chunks(l,n):
    '''chunk l in n sized bits'''
    #http://stackoverflow.com/a/3226719
    #...not that this is hard to understand.
    return [l[x:x+n] for x in xrange(0, len(l), n)];

def check_vprint(s, vprinter):
    '''checked verbose printing'''
    if vprinter is True:
        print(s);
    elif callable(vprinter):
        vprinter(s);

def mkvprint(opts):
    '''makes a verbose printer for use with docopts'''
    return lambda s: check_vprint(s,opts['--verbose']);
 
def subcall(cmd):
    '''check output into list'''
    return subprocess.check_output(cmd).split('\n');

def filelines(fname,strip=False):
    '''read lines from a file into lines...optional strip'''
    with open(fname,'r') as f:
        lines = f.readlines();
    if strip:
        lines[:] = [line.strip() for line in lines]
    return lines;

fltrx_s=r"[-+]{0,1}\d+\.{0,1}\d*(?:[eE][-+]{0,1}\d+){0,1}";
fltrx=re.compile(fltrx_s);

def parse_ftuple(s,length=2,scale=1):
    '''parse a string into a list of floats'''
    rx = r"\( *"+' *, *'.join([fltrx_s]*length)+r" *\)";
    if re.match(rx,s) is None:
        raise ValueError("{} does not match \"{}\".".format(s,rx));
    return [x*scale for x in eval(s)];

