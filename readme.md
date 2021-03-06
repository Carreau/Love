# Love Python Packaging

This is a simple tool which is meant to quickly bootstrap a Python package, and
make most of the manual step of creating a Python package painless.  It is
highly non-configurable, because good library are opinionated (but you can
prove me my default are wrong). So it should work out of the box. 

# Usage:

```
$ love [packagename]
```

If you don't provide a package name, it will provide one for you.

Then it :
    - Checks the name is not taken on PyPI
    - Set up the GitHub repository
    - Clone repository locally
    - Enable Travis.
    - Create a minimal project layout
    - Setup the package using [flit](http://flit.readthedocs.org/en/latest/)

You now just need to focus on coding. 

## Name on PyPI. 

Love will also warn you if your package has a name close to an already published one.
Eg (`panda` too close to `pandas`)

## Travis and GitHub

Love will ask you to provide a Github Token to log in to Travis & GitHub, it
will open a GitHub Page to generate a token, and try to store this token in
your keychain.

# Todo

- setup docs (readthedocs)
- setup dev env ?
- setup tests ?
- setup readme + badges ?
- setup coverage (codecov.io)

# Logo:

```
                  L       OOO    V   V  EEEEE
                  L      O   O   V   V  E
                  L      O   O   V   V  EEE
                  L      O   O    V V   E
      oo          LLLLL   OOO      V    EEEEE
         oo
            oo     OOOOOOOO:       OOOOOOOO!
               oOOOO!!!!;;;;O    OO.......:;!O
              'OOO!!!;;;;;;;;O  O.......:   ;!O
              OOO!!!!;;::::::.OO........:    ;!O
              OO!!!!;;:::::..............:   ;!O
              OOO!!!;::::::..............:   ;!O
               OO!!;;::::::.............:   ;!O           Made With Love
                OO!;;::::::......oo.....::::!O
                  O!!;::::::........oo..:::O                  - M -
                    !!!;:::::..........ooO
                       !!;:::::.......O   oo              version : 0.0.2
                         ;;::::.....O        oo  ,o
                            :::..O              ooo
                              ::.              oooo
                               :
```

