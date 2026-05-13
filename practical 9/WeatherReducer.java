import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class WeatherReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        long sum = 0, count = 0;
        for (LongWritable val : values) {
            sum += val.get();
            count++;
        }
        long avg = sum / count;
        context.write(key, new LongWritable(avg));
    }
}