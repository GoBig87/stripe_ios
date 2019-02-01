from toolchain import CythonRecipe, shprint
from os.path import join
from distutils.dir_util import copy_tree
from shutil import copyfile
import fnmatch
import sh
import os

class StripeRecipe(CythonRecipe):
    version = "1.0.0"
    url = "https://github.com/GoBig87/Stripe_iOS_Wrapper/archive/{version}.zip"
    library = "libstripe.a"
    pbx_frameworks = ['Foundation','Stripe']
    depends = ["python","hostpython"]
    pre_build_ext = True
    archs = ['arm64']
    
    def install(self):
        pass
        arch = list(self.filtered_archs)[0]
        build_dir = join(self.get_build_dir(arch.arch),'build','lib.macosx-10.13-x86_64-2.7')
        filename = '__init__.py'
        with open(os.path.join(build_dir, filename), 'wb'):
            pass
        dist_dir  = join(self.ctx.dist_dir,'root','python','lib','python2.7','site-packages','stripe')
        copy_tree(build_dir, dist_dir)
    
    def make_lipo(self, filename, library=None):
        #Skip this since it's only one Arch
        pass

recipe = StripeRecipe()
