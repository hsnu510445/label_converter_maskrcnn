# label_converter_maskrcnn

origin  
|-label.png : 舊的mask圖  
|-label_names.txt : 舊的圖片所匹配的標籤順序  
new  
|-label_names.txt : 新的圖片所匹配的標籤順序  
  
然後在new裡面生成新的圖片  
  
簡單來說就是換mask的顏色，因為當初在標籤的時候生成的標籤順序可能不太一樣，這樣可能會亂掉  