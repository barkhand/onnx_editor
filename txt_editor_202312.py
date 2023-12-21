from argparse import ArgumentParser
import json

def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--nodename", type=str, required=False, help="Name of the node to delete")
    parser.add_argument("--filename", type=str, required=True, help="Name of file to edit")
    parser.add_argument("--nodefile", type=str, required=False, default=None, help="File of the nodename to delete")
    parser.add_argument("--replacefile", type=str, required=False, default=None, help="File of the lines to replace")
    parser.add_argument("--mode", type=str, required=True, default="replace" , help="replace or delete")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    
    your_file = args.filename
    node_name_to_delete = args.nodename
    mode = args.mode
    start_graph = 'graph {'
    start_node = '  node {\n'
    end_node = '  }\n'
    in_graph = False
    updated_lines = []
    temp_lines = []
    current_status=False
    nodes_to_delete = []
    all_parts=[]

    if args.nodefile!=None:
        if mode=="delete":
            with open(args.nodefile, 'r') as file2:
                for line2 in file2:
                    nodes_to_delete.append(line2)
        else:
            with open(args.replacefile, 'r') as file3:
                additional_line='name: ' 
                for line3 in file3:
                    #lines_to_delete.append(line3)
                    parts = line3.split(',')
                    parts[0]=additional_line+parts[0]
                    all_parts.append(parts)
                    
    
    with open(your_file, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            if start_graph in line:
                in_graph = True
                updated_lines.append(start_graph)
                updated_lines.append('\n')

            if in_graph:
                if mode=='delete': #delete mode:only delete the nodes don't need                   
                    if start_node == line and current_status!=True:
                        current_status=True
                        temp_lines=[] #reset temp_line
                        
                    if any(str(node) in line for node in nodes_to_delete)  and current_status==True:  # Changed to 'in line'
                        current_status=False # wait for the next end_node comes          
                        print(f'Deleting Node:{nodes_to_delete}')
                    if current_status:
                        temp_lines.append(line)
                    if end_node == line:
                        if current_status==False:
                            temp_lines=[]
                        else:
                            updated_lines.append(temp_lines)
                        current_status=False

                elif mode=='replace':
                    if start_node == line and current_status!=True:
                        current_status=True
                        temp_lines=[] #reset temp_line
                    
                    for i in range(len(all_parts)):
                        if all_parts[i][0] in line and current_status:
                            
                            #if any(all_parts[i][1] in element for element in temp_lines): #20231219 problem
                            for j in range(len(temp_lines)):
                                if all_parts[i][1] in temp_lines[j]:
                                    print(f'Deleting Node:{all_parts[i][1]}')
                                    temp_lines[j]=all_parts[i][2]
                                    
                            
                                
                    if current_status:
                        temp_lines.append(line)
                    if end_node == line:
                        if current_status==False:
                            temp_lines=[]
                        else:
                            updated_lines.append(temp_lines)
                        current_status=False
                    
                
            else:
                updated_lines.append(line)

            #if end_graph in stripped_line and in_graph:
            #    in_graph = False

    with open(your_file, 'w') as file:
        for line_list in updated_lines:
            # Join the list into a single string with newline characters
            #line_str = "\n".join(line.rstrip('\n') for line in line_list)
            line_str="".join(line_list)
            file.write(line_str)
        file.write("}")
    #with open(your_file, 'w') as file:
#        for line in updated_lines:
 #           file.write(line)

if __name__ == "__main__":
    main()
