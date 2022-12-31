# frozen_string_literal: true

require 'sinatra'
require_relative 'Map'

set :bind, '0.0.0.0'
set :port, 9999

get '/' do
  'Use /generate with parameters height and width to generate tile map!'
end

get '/generate' do
  map = Map.new(params[:height].to_i, params[:width].to_i)
  data = {}
  map.mapa.each do |key, row|
    tiles = []
    row.each do |tile|
      tiles << tile.type.last
    end
    data.store(key, tiles)
  end
  data.to_json
end
