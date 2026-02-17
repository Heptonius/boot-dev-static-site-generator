from extraction import extract_markdown_images
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node.text = node.text

        images = extract_markdown_images(node.text)
        img_positions = []
        
        for image in images:
            alt_text, url= image
            img_tag = f"![{alt_text}]({url})"
            start_pos = node.text.find(img_tag)
            end_pos = start_pos + len(img_tag)

            img_positions.append((start_pos, end_pos, image))

        cursor_pos = 0

        while cursor_pos < len(node.text):
            next_img_position = None
            
            for img_pos in img_positions:
                start_pos = img_pos[0]
                if start_pos > cursor_pos:
                    next_img_position = img_pos
                    break

            if next_img_position is None:
                # Either no image was found altogether or all image positions were prior to current cursor position
                new_nodes.append(TextNode(node.text[cursor_pos:len(node.text)], TextType.TEXT))
                break
            else: 
                next_img_start_pos, end, image  = next_img_position
                alt_text, url = image
                new_nodes.append(TextNode(node.text[cursor_pos:next_img_start_pos], TextType.TEXT))
                new_nodes.append(TextNode(alt_text,TextType.IMAGE, url))
                cursor_pos = end
            
    
    return new_nodes