import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class WeatherMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] parts = line.split(",");
        if (parts.length >= 2) {
            String year = parts[0].trim();
            long temp = Long.parseLong(parts[1].trim());
            context.write(new Text(year), new LongWritable(temp));
        }
    }
}