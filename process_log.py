import re

def process_log_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontra todas as entradas que começam com data
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}.*?)(?=\d{4}-\d{2}-\d{2}|\Z)'
    log_entries = re.findall(pattern, content, re.DOTALL)
    
    timestamps = []
    for entry in log_entries:
        if 'NOME_DO_ENDPOINT' in entry:
            # Extrai apenas o timestamp do início da entrada
            timestamp_match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})', entry)
            if timestamp_match:
                timestamps.append(timestamp_match.group(1))
    
    # Write filtered timestamps to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(timestamps))

if __name__ == '__main__':
    input_file = 'log.txt'
    output_file = 'log_convertido_py.txt'
    process_log_file(input_file, output_file)
