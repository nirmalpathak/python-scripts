#!/usr/bin/env python
"""
Script to get HTTP headers and set the HTTP headers of AWS S3 obejcts using boto v2.48.0
"""

from boto.s3.connection import S3Connection #Using boto v2.48.0

#--- AWS credentials ----------------------------------------------
AWS_KEY = ''
AWS_SECRET = ''
AWS_BUCKET_NAME = ''

#--- Main function ----------------------------------------------
def main():
    s3_conn = S3Connection(AWS_KEY, AWS_SECRET)

    bucket = s3_conn.get_bucket(AWS_BUCKET_NAME)

    bucket.make_public()
    for key in bucket:
        
        key = bucket.get_key(key.name)

	if key is not None:
            print key
            #print key.cache_control, key.content_type, key.expires
            if key.cache_control is None or key.expires is None:
                print "\033[1;31mNo Cache Control & Expires headers are set!\033[1;m"
                metadata = key.metadata
                metadata['Cache-Control'] = 'max-age=%d, public' % (60 * 60 * 24 * 180) # Set Cache-Control Value to 60 x 60 x 24 x 180 = 6 Months
                metadata['Expires'] = 'Fri, 15 Feb 2019 16:00:00 GMT' # Setting Expires Metadata date & time.
                metadata['Content-Type'] =  key.content_type # Keeping existing Content-Type.
                key.copy(AWS_BUCKET_NAME, key, metadata=metadata, preserve_acl=True)
                print metadata
                print key.name, key.cache_control, key.content_type, key.expires
            else:
                print "\033[1;32mEverything set!\033[1;m"
                print key.name, key.cache_control, key.content_type, key.expires

if __name__ == '__main__':
    main()
