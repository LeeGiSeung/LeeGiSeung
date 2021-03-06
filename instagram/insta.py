import json
import urllib
import requests
import numpy as np

slice_content_result = np.array([])
slice_content = np.array([])


def search_by_tag(words):
    url = ('https://www.instagram.com/explore/tags/%s/?__a=1' % (urllib.parse.quote(words)))
    res = requests.get(url).text
    json_data = json.loads(res)

    print("[ Search Tag for %s ]" % words)

    for c, item in enumerate(json_data['graphql']['hashtag']['edge_hashtag_to_media']['edges']):
        if c == 5:
            break

        #print("[ %s ]" % str(c+1))
        for content in item['node']['edge_media_to_caption']['edges']:
            global slice_content
            global slice_content_result
            raw = content['node']['text']
            slice_content = raw.split()
            slice_content_result = np.append(slice_content_result,slice_content)
            #print("내용: "+ str(slice_content_result))
        #print("짧은 URL: %s" % str('https://www.instagram.com/p/' + item['node']['shortcode']))
        #print("사진 URL: %s" % str(item['node']['display_url']))
        #print("내용: "+ str(slice_content)) 

        print("총 내용: "+ str(slice_content_result))
    #print(slice_content_result[52])


def main():
    search_by_tag('맛집')


if __name__ == '__main__':
    main()