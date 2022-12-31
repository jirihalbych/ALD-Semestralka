# frozen_string_literal: true

require_relative 'Tile'

# Creates Map of Tiles on initialization and assigns their types
class Map
  attr_reader :mapa

  def initialize(height, width)
    @height = height
    @width = width
    @mapa = Hash[(0...height).map { |key| [key, Array.new(width)] }]
    @mapa.each { |key, row| row.map.with_index { |_value, index| placetile(key, index) } }
  end

  def placetile(x, y)
    possible = [[1, 1, 1, 1, 'TILE1'], [0, 0, 0, 1, 'TILE2'], [1, 0, 0, 1, 'TILE3'], [1, 0, 1, 0, 'TILE4'],
                [0, 1, 1, 0, 'TILE5'], [0, 0, 0, 0, 'TILE6'],[1, 1, 0, 0, 'TILE7'],[0, 0, 1, 1, 'TILE8']]
    backtrace = []
    current = @mapa[x][y] ||= Tile.new
    above = current.above = x.zero? ? nil : @mapa[x - 1][y]
    bellow = current.bellow = x == @height - 1 ? nil : @mapa[x + 1][y]
    left = current.left = y.zero? ? nil : @mapa[x][y - 1]
    right = current.right = y == @width - 1 ? nil : @mapa[x][y + 1]
    unless above.nil?
      backtrace << [x - 1, y]
      possible.delete_if { |tile| tile[0] != above.type[1] }
    end
    unless bellow.nil?
      backtrace << [x + 1, y]
      possible.delete_if { |tile| tile[1] != bellow.type[0] }
    end
    unless left.nil?
      backtrace << [x, y - 1]
      possible.delete_if { |tile| tile[2] != left.type[3] }
    end
    unless right.nil?
      backtrace << [x, y + 1]
      possible.delete_if { |tile| tile[3] != right.type[2] }
    end
    if possible.empty?
      replace = backtrace.sample
      placetile(replace[0], replace[1])
      placetile(x, y)
    end
    current.type = possible.sample
  end
end
