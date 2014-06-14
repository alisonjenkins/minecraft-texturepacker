#!/usr/bin/env python3
import zipfile
import tempfile
import shutil
import os
import os.path

class TexturePacker(object):
    def __init__(self, texturepack, output_path, patches):
        self.texturepack = texturepack
        self.output_path = output_path
        texture_pack_patches = patches

        self.packs_path = os.path.join(os.path.realpath(__file__), 'texture_packs')
        self.patched_packs = os.path.join(os.path.realpath(__file__), 'patched_packs')
        self.patches_path = os.path.join(os.path.realpath(__file__), 'patches')

    def patch_pack(self):
        # copy existing pack to temp dir
        output_temp = tempfile.mkdtemp()

        # setup paths
        tempoutput_path = os.path.join(output_temp, os.path.split(output_path[1]))

        # copy the pack zip file to output_temp
        shutil.copy(os.path.join(self.packs_path, self.texturepack), tempoutput_path)

        with ZipFile(tempoutput_path, 'w') as tpzf:
            # for each patch file
            for patch in self.texture_pack_patches:
                # Make temp directory for extracting the path
                patch_temp = tempfile.mkdtemp()

                # extract the patch
                with ZipFile(patch, 'r') as pzf:
                    pzf.extractall(patch_temp)

                # # add all the files and folders in the patch to the pack
                # for root, dirs, files in os.walk(patch_temp):
                #


                # delete the patch_temp dir

            # move the patched pack to the output path

patches = ['Griffs Sphax 64x v15 for RR MC16 ADDON.zip']
tpp = TexturePacker('Sphax PureBDcraft  64x MC18.zip', 'Sphax PureBDcraft  64x MC18 patched.zip', patches)
