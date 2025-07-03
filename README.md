# mt_test_framework
metamorphic testing framework


## usage 
```
sh run_mt.sh 10 light
```
to generate 10 test sequences for smart light devide

```
sh run_mt.sh 10 tv 
```
to generate 10 test sequences for smart tv 

```

mut.py \
  --target 3rd.sinric_python.sinric \
          utils.config_io \
          http_req.action_req \
  --unit-test tests/ \
  -m -e --runner pytest --report-html REPORT

```

to run mutation test.
