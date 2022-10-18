# Практическое задание (веб-скрапинг)

Скрипт обращается к [Google Scholar](https://scholar.google.com/). Сохраняет результаты поиска в csv файл (название статьи, описание, ссылка).

## Установка

Для использования скрипта необходимы три пакета.

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
```

## Использование

```python
# сохраняет результаты первой страницы поиска по запросу "microservices" в файл results.csv
python scraper.py 'microservices'

# сохраняет результаты первых двух страниц поиска
python scraper.py 'microservices' 2

```

## Пример result.csv

```csv
title,desc,link
"Microservices: yesterday, today, and tomorrow","Microservices is an architectural style inspired by service-oriented computing that has recently
started gaining popularity. Before presenting the current state of the art in the field, this …",https://arxiv.org/pdf/1606.04036
Microservices,"… Tilkov discusses architecture and microservices; in episode … covering the relationship between
microservices and Conway’s … I think it’s about the right time for an idea like microservices …",https://ieeexplore.ieee.org/iel7/52/7030140/07030212.pdf
Microservices tenets,"… ) and microservices has been reached so far. This paper argues that microservices concepts
… This review started with the reading list and the outcomes of a microservices workshop at …",https://www.ifsoftware.ch/uploads/tx_icscrm/1_msa-pospaperzio4summersoc2016v15nc.pdf
Microservices: The journey so far and challenges ahead,"… In contrast, microservices typically rely on REST (Represen… integration solution, whereas
microservices are typically applied … Here, we look at microservices’ evolution from both the …",https://ieeexplore.ieee.org/iel7/52/8354413/08354433.pdf
Microservices: How to make your application scale,"… In this paper, we describe the main features of microservices and … other microservices, those
microservices will be affected. Therefore one should be careful when placing microservices …",https://arxiv.org/pdf/1702.07149
Performance engineering for microservices: research challenges and directions,"… for microservices in this paper. To start with, we discuss in Section 2 specific characteristics
of microservices and … engineering for microservices (Section 3) and conclude this paper. …",https://oceanrep.geomar.de/id/eprint/37428/1/HeinrichvanHoornKnocheLiLwakatarePahlSchulteWettinger2017PerformanceEngineeringForMicroservicesResearchChallengesAndDirections-publisher.pdf
