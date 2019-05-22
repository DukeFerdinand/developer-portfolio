require 'bundler/setup'

require 'sinatra'

# Config section
configure { set :server, :puma }
set :root, 'dist'
set :public_folder, 'dist'

get '/api' do
  "Hello from ruby!"
end

get '*' do
  puts File.expand_path('index.html', settings.public_folder)
  send_file File.expand_path('index.html', settings.public_folder)
end