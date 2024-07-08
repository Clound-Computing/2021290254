+ python -u gnncl.py --feature profile --epochs 60 --lr 0.001 --nhid 128 --batch_size 128 --dataset politifact
Namespace(batch_size=128, dataset='politifact', epochs=60, feature='profile', lr=0.001, nhid=128, seed=777, weight_decay=0.001)

  0%|          | 0/60 [00:00<?, ?it/s]loss_train: 0.7162, acc_train: 0.4355, recall_train: 0.1538, auc_train: 0.3643, loss_val: 21.9282, acc_val: 0.4194, recall_val: 0.0000, auc_val: 0.6239

  2%|▏         | 1/60 [00:00<00:31,  1.88it/s]
  3%|▎         | 2/60 [00:00<00:29,  1.97it/s]loss_train: 0.6253, acc_train: 0.7097, recall_train: 0.3846, auc_train: 0.8269, loss_val: 21.9557, acc_val: 0.4194, recall_val: 0.0000, auc_val: 0.6197
loss_train: 0.5658, acc_train: 0.8548, recall_train: 0.6923, auc_train: 0.9209, loss_val: 21.8240, acc_val: 0.4194, recall_val: 0.0000, auc_val: 0.7094

  5%|▌         | 3/60 [00:01<00:27,  2.09it/s]loss_train: 0.5146, acc_train: 0.8871, recall_train: 0.7308, auc_train: 0.9583, loss_val: 21.6586, acc_val: 0.4194, recall_val: 0.0000, auc_val: 0.7009

  7%|▋         | 4/60 [00:01<00:25,  2.19it/s]loss_train: 0.4586, acc_train: 0.8710, recall_train: 0.7308, auc_train: 0.9882, loss_val: 21.4691, acc_val: 0.4516, recall_val: 0.0556, auc_val: 0.6923

  8%|▊         | 5/60 [00:02<00:24,  2.25it/s]
 10%|█         | 6/60 [00:02<00:23,  2.31it/s]loss_train: 0.4000, acc_train: 0.9355, recall_train: 0.8462, auc_train: 0.9979, loss_val: 21.2227, acc_val: 0.5806, recall_val: 0.3889, auc_val: 0.6838

 12%|█▏        | 7/60 [00:03<00:22,  2.35it/s]loss_train: 0.3416, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 20.9328, acc_val: 0.7097, recall_val: 0.7222, auc_val: 0.6966

 13%|█▎        | 8/60 [00:03<00:21,  2.38it/s]loss_train: 0.2848, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 20.6299, acc_val: 0.6452, recall_val: 0.9444, auc_val: 0.7137

 15%|█▌        | 9/60 [00:03<00:21,  2.40it/s]loss_train: 0.2317, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 20.3748, acc_val: 0.5806, recall_val: 0.9444, auc_val: 0.7009
loss_train: 0.1820, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 20.2128, acc_val: 0.5806, recall_val: 1.0000, auc_val: 0.6838

 17%|█▋        | 10/60 [00:04<00:20,  2.41it/s]
 18%|█▊        | 11/60 [00:04<00:20,  2.41it/s]loss_train: 0.1454, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 20.2176, acc_val: 0.6129, recall_val: 1.0000, auc_val: 0.6581
loss_train: 0.1156, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 20.3346, acc_val: 0.6129, recall_val: 1.0000, auc_val: 0.6410

 20%|██        | 12/60 [00:05<00:19,  2.42it/s]loss_train: 0.0909, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 20.5211, acc_val: 0.5484, recall_val: 0.8889, auc_val: 0.6368

 22%|██▏       | 13/60 [00:05<00:19,  2.43it/s]
 23%|██▎       | 14/60 [00:05<00:18,  2.44it/s]loss_train: 0.0708, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 20.8210, acc_val: 0.5161, recall_val: 0.7778, auc_val: 0.6410

 25%|██▌       | 15/60 [00:06<00:18,  2.43it/s]loss_train: 0.0539, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 21.3054, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.6325

 27%|██▋       | 16/60 [00:06<00:18,  2.44it/s]loss_train: 0.0409, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 22.0058, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.6368
loss_train: 0.0307, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 23.0507, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.6282

 28%|██▊       | 17/60 [00:07<00:17,  2.44it/s]loss_train: 0.0232, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 24.4001, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.6197

 30%|███       | 18/60 [00:07<00:17,  2.45it/s]
 32%|███▏      | 19/60 [00:07<00:16,  2.45it/s]loss_train: 0.0175, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 25.9041, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.6068

 33%|███▎      | 20/60 [00:08<00:16,  2.44it/s]loss_train: 0.0133, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 27.5945, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.5983

 35%|███▌      | 21/60 [00:08<00:15,  2.45it/s]loss_train: 0.0102, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 29.4583, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.5769
loss_train: 0.0079, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 31.5018, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.5641

 37%|███▋      | 22/60 [00:09<00:15,  2.45it/s]loss_train: 0.0061, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 33.4855, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.5726

 38%|███▊      | 23/60 [00:09<00:15,  2.45it/s]loss_train: 0.0047, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 35.6020, acc_val: 0.5484, recall_val: 0.7778, auc_val: 0.5641

 40%|████      | 24/60 [00:09<00:14,  2.45it/s]
 42%|████▏     | 25/60 [00:10<00:14,  2.44it/s]loss_train: 0.0037, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 38.2323, acc_val: 0.5484, recall_val: 0.7222, auc_val: 0.5556
loss_train: 0.0030, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 41.5995, acc_val: 0.5484, recall_val: 0.6667, auc_val: 0.5598

 43%|████▎     | 26/60 [00:10<00:13,  2.45it/s]
 45%|████▌     | 27/60 [00:11<00:13,  2.45it/s]loss_train: 0.0025, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 45.3512, acc_val: 0.5161, recall_val: 0.6111, auc_val: 0.5641
loss_train: 0.0020, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 49.2481, acc_val: 0.5161, recall_val: 0.6111, auc_val: 0.5726

 47%|████▋     | 28/60 [00:11<00:13,  2.44it/s]
 48%|████▊     | 29/60 [00:12<00:12,  2.45it/s]loss_train: 0.0017, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 53.9049, acc_val: 0.4839, recall_val: 0.5556, auc_val: 0.5812

 50%|█████     | 30/60 [00:12<00:12,  2.44it/s]loss_train: 0.0014, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 59.3107, acc_val: 0.4839, recall_val: 0.5556, auc_val: 0.5812

 52%|█████▏    | 31/60 [00:12<00:11,  2.45it/s]loss_train: 0.0012, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 65.4227, acc_val: 0.4839, recall_val: 0.5556, auc_val: 0.5855
loss_train: 0.0010, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 71.7496, acc_val: 0.4839, recall_val: 0.5556, auc_val: 0.5812

 53%|█████▎    | 32/60 [00:13<00:11,  2.45it/s]loss_train: 0.0009, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 77.9757, acc_val: 0.5161, recall_val: 0.5556, auc_val: 0.5855

 55%|█████▌    | 33/60 [00:13<00:11,  2.44it/s]
 57%|█████▋    | 34/60 [00:14<00:10,  2.44it/s]loss_train: 0.0008, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 84.2176, acc_val: 0.5161, recall_val: 0.5556, auc_val: 0.5769

 58%|█████▊    | 35/60 [00:14<00:10,  2.44it/s]loss_train: 0.0007, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 90.1566, acc_val: 0.5161, recall_val: 0.5556, auc_val: 0.5684

 60%|██████    | 36/60 [00:14<00:09,  2.45it/s]loss_train: 0.0006, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 95.2013, acc_val: 0.5161, recall_val: 0.5556, auc_val: 0.5598
loss_train: 0.0005, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 99.3444, acc_val: 0.5161, recall_val: 0.5556, auc_val: 0.5427

 62%|██████▏   | 37/60 [00:15<00:09,  2.44it/s]
 63%|██████▎   | 38/60 [00:15<00:08,  2.45it/s]loss_train: 0.0005, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 102.7257, acc_val: 0.5161, recall_val: 0.5556, auc_val: 0.5470

 65%|██████▌   | 39/60 [00:16<00:08,  2.45it/s]loss_train: 0.0004, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 105.5426, acc_val: 0.5161, recall_val: 0.5556, auc_val: 0.5385

 67%|██████▋   | 40/60 [00:16<00:08,  2.45it/s]loss_train: 0.0004, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 108.4309, acc_val: 0.5161, recall_val: 0.5556, auc_val: 0.5256
loss_train: 0.0004, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 110.9903, acc_val: 0.4839, recall_val: 0.5000, auc_val: 0.5171

 68%|██████▊   | 41/60 [00:16<00:07,  2.45it/s]
 70%|███████   | 42/60 [00:17<00:07,  2.45it/s]loss_train: 0.0003, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 112.7643, acc_val: 0.4839, recall_val: 0.5000, auc_val: 0.5256

 72%|███████▏  | 43/60 [00:17<00:06,  2.46it/s]loss_train: 0.0003, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 114.0549, acc_val: 0.4839, recall_val: 0.5000, auc_val: 0.5214

 73%|███████▎  | 44/60 [00:18<00:06,  2.46it/s]loss_train: 0.0003, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 115.2468, acc_val: 0.4839, recall_val: 0.5000, auc_val: 0.5256
loss_train: 0.0003, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 116.7893, acc_val: 0.4839, recall_val: 0.4444, auc_val: 0.5299

 75%|███████▌  | 45/60 [00:18<00:06,  2.45it/s]
 77%|███████▋  | 46/60 [00:18<00:05,  2.45it/s]loss_train: 0.0003, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 118.4344, acc_val: 0.5161, recall_val: 0.5000, auc_val: 0.5342

 78%|███████▊  | 47/60 [00:19<00:05,  2.44it/s]loss_train: 0.0003, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 119.9254, acc_val: 0.4839, recall_val: 0.4444, auc_val: 0.5427
loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 121.4900, acc_val: 0.5161, recall_val: 0.4444, auc_val: 0.5556

 80%|████████  | 48/60 [00:19<00:04,  2.45it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 122.6518, acc_val: 0.5484, recall_val: 0.5000, auc_val: 0.5598

 82%|████████▏ | 49/60 [00:20<00:04,  2.45it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 123.0104, acc_val: 0.5484, recall_val: 0.5000, auc_val: 0.5769

 83%|████████▎ | 50/60 [00:20<00:04,  2.45it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 122.4748, acc_val: 0.5161, recall_val: 0.4444, auc_val: 0.5812

 85%|████████▌ | 51/60 [00:21<00:03,  2.45it/s]
 87%|████████▋ | 52/60 [00:21<00:03,  2.43it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 121.0283, acc_val: 0.5161, recall_val: 0.4444, auc_val: 0.5897
loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 118.4664, acc_val: 0.5484, recall_val: 0.4444, auc_val: 0.5897

 88%|████████▊ | 53/60 [00:21<00:02,  2.42it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 115.2615, acc_val: 0.5484, recall_val: 0.4444, auc_val: 0.6068

 90%|█████████ | 54/60 [00:22<00:02,  2.43it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 111.4406, acc_val: 0.5806, recall_val: 0.5000, auc_val: 0.6239

 92%|█████████▏| 55/60 [00:22<00:02,  2.43it/s]
 93%|█████████▎| 56/60 [00:23<00:01,  2.44it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 107.6296, acc_val: 0.6129, recall_val: 0.5000, auc_val: 0.6239
loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 104.2249, acc_val: 0.6452, recall_val: 0.5556, auc_val: 0.6368

 95%|█████████▌| 57/60 [00:23<00:01,  2.43it/s]
 97%|█████████▋| 58/60 [00:23<00:00,  2.44it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 101.1076, acc_val: 0.6452, recall_val: 0.5556, auc_val: 0.6410
loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 97.9543, acc_val: 0.6452, recall_val: 0.5556, auc_val: 0.6496

 98%|█████████▊| 59/60 [00:24<00:00,  2.44it/s]loss_train: 0.0002, acc_train: 1.0000, recall_train: 1.0000, auc_train: 1.0000, loss_val: 94.7665, acc_val: 0.6129, recall_val: 0.5556, auc_val: 0.6667

100%|██████████| 60/60 [00:24<00:00,  2.45it/s]
politifact GNNCL Testing Results:
acc: 0.6018, f1_macro: 0.5922, f1_micro: 0.6018, precision: 0.6477, recall: 0.4646, auc: 0.7257, ap: 0.7293