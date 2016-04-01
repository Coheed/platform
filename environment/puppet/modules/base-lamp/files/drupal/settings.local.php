<?php

$databases['default']['default'] = array(
  'driver' => 'mysql',
  'host' => 'localhost',
  'username' => 'root',
  'password' => '',
  'database' => 'berkshireinnovationcenter',
  'prefix' => '',
);


$conf['cache'] = 0;
$conf['block_cache'] = 0;
$conf['preprocess_css'] = 0;
$conf['preprocess_js'] = 0;

$conf['search_api_override_mode'] = 'load';
$conf['search_api_override_servers'] = array(
  'solr_service' => array(
    'name' => 'Solr service (overriden)',
    'options' => array(
      'host' => 'localhost',
      'port' => '8080',
      'path' => '/solr',
      'http_user' => '',
      'http_pass' => '',
      'excerpt' => 0,
      'retrieve_data' => 0,
      'highlight_data' => 0,
      'http_method' => 'POST',
    ),
  ),
);