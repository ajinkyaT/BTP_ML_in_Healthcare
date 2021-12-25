from os.path import splitext, join


def join_datasets(
    in_filenames: 'list[str]',
    in_directory: str,
    out_filepath: str
) -> None:
    '''
    Join the files in the cleveland, hungarian, long-beach-va, and
    switzerland databases after a final cleaning to remove incomplete records.
    Input files are assumed to be in the `in_directory`.  Output file goes
    to `out_directory`.
    '''

    out_file = open(out_filepath, 'w')
    total_input = 0
    total_output = 0
    for in_filename in in_filenames:
        input_file = open(join(in_directory, in_filename), 'r')
        nlines_through = 0
        nlines_total = 0
        for line in input_file:
            total_input += 1
            nlines_total += 1
            if ("-9" not in line) and ("?" not in line):
                features_list = line.split(",")
                features_list = [float(item) for item in features_list[0:14]]
                corrected_line = ",".join(map(str, features_list))
                out_file.write(corrected_line+"\n")
                total_output += 1
                nlines_through += 1
        print('Transferred {} out of {} records from {}'.format(
            nlines_through,
            nlines_total,
            in_filename))
        input_file.close()
    out_file.close()

    print(f'Total records read in: {total_input}')
    print(f'Total records written out to {out_filepath}: {total_output}')


def convert_ssc_to_csv(
    filename: str,
    in_directory: str,
    out_directory: str
) -> None:
    '''
    Convert a space-separated file into a comma-separated file.
    Keeps the same name: file.ssv -> file.csv.
    '''

    def base_filename(filename: str) -> str:
        return splitext(filename)[0]

    filepath_ssc = join(in_directory, filename)
    filepath_csv = join(out_directory, base_filename(filename) + '.csv')

    file_ssc = open(filepath_ssc, 'r')
    file_csv = open(filepath_csv, 'w')

    for line in file_ssc:
        if line.strip():
            line = line.replace(" ", ",")
            file_csv.write(line)

    file_ssc.close()
    file_csv.close()
