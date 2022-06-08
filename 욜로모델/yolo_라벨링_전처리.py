# txt 내용 바꾸기
def replace_in_file(file_path, old_str, new_str):
    # 파일 읽어들이기
    fr = open(file_path, 'r')
    lines = fr.readlines()
    lines = lines[1]
    fr.close()
    
    # old_str -> new_str 치환
    fw = open(file_path, 'w')
    fw.write(lines.replace(old_str, new_str))
    fw.close()