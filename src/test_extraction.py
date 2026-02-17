import unittest

from extraction import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):
    def test_md_image_extraction_empty(self):
        images_found = extract_markdown_images("")
        self.assertEqual(images_found, [])

    def test_md_image_extraction(self):
        md_sample = """# This is a heading
        ![image alt text](https://img.cdn.com/asdasd/123) 

        This is a random text
        ![second img](https://img.cdn.com/asdasd/234) 

        This is a link:
        [link anchor text](https://cool.link/path)
        """
        images_found = extract_markdown_images(md_sample)
        self.assertEqual(images_found, [('image alt text', 'https://img.cdn.com/asdasd/123'), ('second img', 'https://img.cdn.com/asdasd/234')])

    def test_another_case_image_extraction(self):
        md_sample = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
        
        images_found = extract_markdown_images(md_sample)
        self.assertEqual(images_found, [("image", "https://i.imgur.com/zjjcJKZ.png"),("second image", "https://i.imgur.com/3elNhQu.png")])
        
class TestExtractMarkdownLinks(unittest.TestCase):
    def test_md_link_extraction_empty(self):
        links_found = extract_markdown_links("")
        self.assertEqual(links_found, [])

    def test_md_link_extraction(self):
        md_sample = """# This is a heading
        ![image alt text](https://img.cdn.com/asdasd/123) 

        This is a random text
        ![second img](https://img.cdn.com/asdasd/234) 

        This is a link:
        [link anchor text](https://cool.link/path)
        """
        links_found = extract_markdown_links(md_sample)
        self.assertEqual(links_found, [('link anchor text', 'https://cool.link/path')])    

if __name__ == "__main__":
    unittest.main()