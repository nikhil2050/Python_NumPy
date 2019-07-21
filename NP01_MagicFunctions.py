import matplotlib.pyplot as plt
%matplotlib inline

plt.plot([1,2,3,4])
plt.xlabel("x")
plt.ylabel("y")
plt.show()

magic

# Profile code
%timeit 2**128          # 349 ns ± 9.32 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%pwd          # 'C:\\Users\\10643821\\NKPythonNotebook\\190711_iLearn_Numpy'

%cd D:\NKPythonNotebook

# To start both mat.lib and numpy in interactive mode
%pylab
# Using matplotlib backend: Qt5Agg
# Populating the interactive namespace from numpy and matplotlib

# --------------- list of magic functions -------------------------
%lsmagic
#Available line magics:
#%alias  %alias_magic  %autocall  %automagic  %autosave  %bookmark  %cd  %clear  %cls  %colors  %config  %connect_info  %copy  %ddir  %debug  %dhist  %dirs  %doctest_mode  %echo  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %macro  %magic  %matplotlib  %mkdir  %more  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %ren  %rep  %rerun  %reset  %reset_selective  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode

#Available cell magics:
# %%!  %%HTML  %%SVG  %%bash  %%capture  %%cmd  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile

#Automagic is ON, % prefix IS NOT needed for line magics.

# --------------- list of magic functions -------------------------

# Quick reference sheet (in new window)
%quickref
