#!/usr/bin/python
import os
from PIL import Image
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting up")

storage_dir = 'items/'
output_dir = 'assets/'
umbrella_class = 'd2items'
logger.info("Working on {0}".format(storage_dir))


def write_sheets():

    #Helper functions
    def css_class(item):
        return ".{0}.{1}".format(umbrella_class, item)

    def calc_position(idx, image_height):
        return image_height*idx*2

    logger.info("Using prefix: {0}".format(umbrella_class))
    objects = []
    for item in os.listdir(storage_dir):
        filename, fileextension = os.path.splitext(item)
        objects.append({
            'name': filename,
            'ext': fileextension,
            'full_name': item,
            'image': Image.open(storage_dir+item),
            'css': css_class(item),
            })

    image_width, image_height = objects[0]['image'].size
    logger.info("Presuming all files {0} wide and {1} high".format(
        image_width, image_height
        )
    )

    spriteimg_width = image_width
    spriteimg_height = (image_height * len(objects) * 2) - image_height
    logger.info("Spritesheet will be {0} wide and {1} high".format(
        spriteimg_height, spriteimg_height
        )
    )

    spritesheet = Image.new(
        mode='RGBA',
        size=(spriteimg_width, spriteimg_height),
        color=(0, 0, 0, 0)
    )  # 100% transparent alpha

    for idx, data in enumerate(objects):
        image = data['image']
        location = calc_position(idx, image_height)

        logger.info("Adding {0} at {1}".format(
            data['name'], location
            )
        )
        spritesheet.paste(image, (0, location))
    logger.info("Done adding.")

    spritesheet.save(output_dir+'spritesheet.gif', transparency=0)
    logger.info("Gif saved.")

    spritesheet.save(output_dir+'spritesheet.png')
    logger.info("Png saved.")

    cssFormat = '''i{css_class} {{
        background-image:url(../images/spritesheet.{suffix});
        background-position: 0px {image_position};
    }}
    '''

    for file_format in ['png', 'gif']:
        iconCssFile = open(output_dir+'icons_{format}.css'.format(
            format=file_format
            ), 'w')
        for idx, data in enumerate(objects):
            css_class = data['css']
            position = calc_position(idx, image_height)
            iconCssFile.write(
                cssFormat.format(
                    css_class=css_class,
                    suffix=file_format,
                    image_position=position
                )
            )
        iconCssFile.close()
        logger.info("{0} saved.".format(file_format))

if __name__ == "__main__":
    write_sheets()
