def generate_report(data, output_file):
    try:
        with open(output_file, 'w') as f:
            f.write("SEO Report\n")
            f.write("=" * 40 + "\n\n")
            for key, value in data.items():
                f.write("{}: {:.2f}%\n".format(key, value))
        print "Report saved to {}".format(output_file)
    except Exception as e:
        print "Error writing report: {}".format(e)
