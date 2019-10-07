package example;

import java.lang.Thread;

import com.amazonaws.services.lambda.runtime.Context;

public class Hello {
    public String handleRequest(Integer lag, Context context) throws InterruptedException {
        Thread.sleep(lag);
        return String.valueOf(lag);
      }
}