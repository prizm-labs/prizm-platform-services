seedCollection( Apps, 'seed', 'apps' );
seedCollection( Channels, 'seed', 'channels' );
seedCollection( Releases, 'seed', 'releases' );

function seedCollection( collection, seedFile, seedObject, iterator ){

    if ( collection.find().count() === 0 ){
        console.log('seeding collection',seedObject);

        var documents = JSON.parse(Assets.getText(seedFile+'.json'))[seedObject];

        _.each( documents, function( doc ){

            if (iterator){
                doc = iterator(doc);
            }

            collection.insert(doc);
        });
    }

}
