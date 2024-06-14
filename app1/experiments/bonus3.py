contents = ['foo', 'bar', 'baz']

filenames = ['bish', 'bash', 'bosh']

for content, filename in zip(contents, filenames):
    with open(f'files/{filename}', 'w') as file:
        file.write(content)
