# Author: Johanan JS
# Date: 6th Dec, 2023
# Purpose: To create youtube playlists easily.

class playlistmaker:
    '''
    Input: Text file containing youtube links. One in every line.
    Ouput: Youtube Playlist. Copy and paste this on your browser.
        It will generate an untitled playlist.
        You can further save this playlist or add to another playlist
        by using the link parameter.
    '''
    def __init__(self, playlistfile):
        self.videolink = None
        self.linklist = []
        self.playlistfile = playlistfile
        self.playlist_string = 'http://www.youtube.com/watch_videos?video_ids='
        self.makeplaylist()
        # print(self.linklist)
        print(self.playlist_string[:-1])


    def makeplaylist(self):
        '''
        Make the playlist from the playlist text file provided.
        '''
        with open(self.playlistfile, 'r') as playlist_io:
            self.playlist = playlist_io.read().splitlines()

        for i in range(len(self.playlist)):
            # print(self.playlist[i])
            self.videolink = self.playlist[i]
            try:
                self.findlinktype()
                self.playlist_string = self.playlist_string + str(self.linklist[-1]) + ","
            except:
                continue
        return True

    def findlinktype(self):
        '''
        There are two types of youtube links as far as I know.
        One that can be copied from the web browser.
        One that is generating when using the share button.
        '''
        if self.videolink.find('youtube') > -1:
            self.browserlink()
        elif self.videolink.find('youtu.be') > -1:
            self.sharelink()
        elif self.videolink[0] == "#":
            return False
        return True

    def browserlink(self):
        '''
        Find the id of the video, when the link is copied from the browser.
        '''
        sidx = self.videolink.find('v=') + 2
        video_id = self.videolink[sidx:]
        self.linklist.append(video_id)
        return video_id

    def sharelink(self):
        '''
        Find the id of the video, when the link is copied from the share feature.
        '''
        sidx = self.videolink.find('.be/') + 4
        eidx = self.videolink.find('?')
        video_id = self.videolink[sidx:eidx]
        self.linklist.append(video_id)
        return video_id
