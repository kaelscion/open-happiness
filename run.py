from app import app
from app import cms
import choose_query

cq = choose_query.data_miner('http://www.google.com/images')
cq.get_query()
cq.get_links(cq.query)
cq.download_files(cq.query)

cm = cms.load_content('app/templates/main.html')
cm.load_new_images()
cm.generate_html()

app.run(debug=True)
