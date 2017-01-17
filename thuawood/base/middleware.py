import datetime
import re
import time

from thuawood.base.fscache import path_to_fs_path, cache_request


max_age_re = re.compile('max-age=(\d+)')


class FSCacheMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if cache_request(request, response):
            fs_path = path_to_fs_path(request.path)
            if not fs_path:
                # exit early
                return response
            try:
                seconds = int(
                    max_age_re.findall(response.get('Cache-Control'))[0]
                )
            except TypeError:
                # exit early fi the cache-control isn't set
                return response
            if seconds > 60:
                metadata_text = 'FSCache {}::{}::{}'.format(
                    int(time.time()),
                    seconds,
                    datetime.datetime.utcnow()
                )
                # Proceed only if it's a long'ish time to be cached
                with open(fs_path, 'w') as f:
                    f.write(response.content.decode('utf-8'))
                    if 'text/html' in response['Content-Type']:
                        f.write('\n<!-- {} -->\n'.format(metadata_text))
                with open(fs_path + '.metadata', 'w') as f:
                    f.write(metadata_text)
                    f.write('\n')
        return response
