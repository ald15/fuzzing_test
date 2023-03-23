# fuzzing_test
My first fuzzing

My commands:

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

export AFL_PYTHON_MODULE=test
afl-fuzz -x /home/ald15/AFLplusplus/dictionaries/html_tags.dict -M Master -i html_examples -o out -- ./tidy -o tidy_out -f tidy_err @@
afl-fuzz -x /home/ald15/AFLplusplus/dictionaries/html_tags.dict -S Slave1 -i html_examples -o out -- ./tidy -o tidy_out -f tidy_err @@
afl-fuzz -x /home/ald15/AFLplusplus/dictionaries/html_tags.dict -S Slave2 -i html_examples -o out -- ./tidy -o tidy_out -f tidy_err @@

Parallel fuzzing
![fuzz](https://user-images.githubusercontent.com/62624802/227179906-c2886b1a-23c5-42d2-8ec1-cdd79375db8b.png)

