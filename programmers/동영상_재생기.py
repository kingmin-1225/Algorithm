def solution(video_len, pos, op_start, op_end, commands):
  ans = ''
  def str2int(time):
    return int(time[:2])*60+int(time[3:])

  def skip(time):
    if op_start <= time < op_end:
      return op_end
    return time
  
  op_start = str2int(op_start)
  op_end = str2int(op_end)
  video_len = str2int(video_len)
  time = str2int(pos)
  
  time = skip(time)
  for command in commands:
    if command == "next":
      time += 10
      time = min(time, video_len)
    else:
      time -= 10
      time = max(0, time)
    time = skip(time)
  minutes = time // 60
  seconds = time % 60
  if minutes < 10:
    ans += '0'
  ans += str(minutes)+':'
  if seconds < 10:
    ans += '0'
  ans += str(seconds)
  return ans