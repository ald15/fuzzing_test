# fuzzing_test
My first fuzzing


Target: https://github.com/htacg/tidy-html5

My commands:
<pre>
cd $HOME
mkdir fuzzing_main
cd fuzzing_main
git clone https://github.com/htacg/tidy-html5
cd tidy-html5/build/cmake
cmake cmake -DCMAKE_C_COMPILER=afl-clang-fast -S ../..
export LLVM_CONFIG="llvm-config-11"
make
mv ./tidy ../../../
cd ../../../
mkdir html_examples
cd html_examples
wget https://filesamples.com/samples/code/html/sample1.html
wget https://filesamples.com/samples/code/html/sample2.html
cd ../
export PYTHONPATH=`dirname /home/ald15/AFLplusplus/custom_mutators/examples/test.py`
export AFL_PYTHON_MODULE=test
afl-fuzz -x /home/ald15/AFLplusplus/dictionaries/html_tags.dict -M Master -i html_examples -o out -- ./tidy -o tidy_out -f tidy_err @@
afl-fuzz -x /home/ald15/AFLplusplus/dictionaries/html_tags.dict -S Slave1 -i html_examples -o out -- ./tidy -o tidy_out -f tidy_err @@
afl-fuzz -x /home/ald15/AFLplusplus/dictionaries/html_tags.dict -S Slave2 -i html_examples -o out -- ./tidy -o tidy_out -f tidy_err @@
afl-fuzz -x /home/ald15/AFLplusplus/dictionaries/html_tags.dict -S Slave3 -i html_examples -o out -- ./tidy -o tidy_out -f tidy_err @@
</pre>

Parallel fuzzing:

<p> <b>[ERROR!]</b>
The first two screenshots contain an error: I started the Master with a mutator, and the others without
</p>

![fuzz](https://user-images.githubusercontent.com/62624802/227179906-c2886b1a-23c5-42d2-8ec1-cdd79375db8b.png)
![fuzz2](https://user-images.githubusercontent.com/62624802/227184239-90b677dd-940a-4b95-9d17-4d0e0246b9dd.png)

<p> <b>Success</b> In the screenshot below, I fixed the problem described above, and also added a few more instances</p>

![fuzz4](https://user-images.githubusercontent.com/62624802/227204726-7b14033a-f989-423c-b513-87d8bec3ae29.png)



