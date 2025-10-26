# Gemfile — Fixed version for Netlify Jekyll Build
source "https://rubygems.org"

# ✅ Cho phép Netlify dùng Ruby bản mới hơn mà không lỗi
ruby ">= 3.3.0"

# ✅ Các gói cần thiết để Jekyll build thành công
gem "jekyll", "~> 4.3.2"
gem "webrick", "~> 1.8"
gem "minima", "~> 2.5"
gem "jekyll-seo-tag", "~> 2.8"
gem "jekyll-feed", "~> 0.17"

# ✅ Plugin cho sitemap và Google indexing
gem "jekyll-sitemap", "~> 1.4"

# ✅ Giúp build mượt hơn trên Netlify
group :jekyll_plugins do
  gem "jekyll-paginate"
end

# ✅ Fix dependency lỗi cho Ruby 3.x
gem "bundler", "~> 2.5"
