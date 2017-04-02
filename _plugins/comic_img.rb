module Jekyll

  class ComicImgPathGenerator < Generator
    safe true
    def generate(site)
      site.posts.docs.each do |post|
        tokens = post.path.split('/')
        comic_img = tokens[-1].sub('.md', '.jpg')
        post.data['comic_img'] = comic_img
        post.data['thumbnail'] = '/images/comics/thumbs/' + comic_img
      end
    end
  end

end