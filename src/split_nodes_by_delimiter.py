from textnode import TextNode, TextType


def split_text_node_by_delimiter(node, delimiter, text_type):
    if node.text_type != TextType.TEXT:
        return [node]
    
    
    parts = node.text.split(delimiter)
    
    # If no delimiter found, return original node
    if len(parts) == 1:
        return [node]
    
    # Check for unclosed delimiter (odd number of parts means unmatched)
    if len(parts) % 2 == 0:
        raise ValueError(f"Unclosed delimiter '{delimiter}' in text")
    
    result = []
    for i, part in enumerate(parts):
        if not part:  # Skip empty strings
            continue
        
        if i % 2 == 0:  # Even indices are normal text
            result.append(TextNode(part, TextType.TEXT))
        else:  # Odd indices are delimited content
            result.append(TextNode(part, text_type))
    
    return result

def split_nodes_by_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        split_node = split_text_node_by_delimiter(node, delimiter, text_type)
        new_nodes.extend(split_node)

    return new_nodes

