class HomePostInfo extends React.Component{
    render(){
        return(
            <div class="col-xs-12 col-sm-12 col-md-6">
                <div class="card fade-in">
                    <div class="card-viewed">
                        <i class="fa fa-eye" aria-hidden="true"></i>&nbsp{{ post.viewed }}
                    </div>
                    <a class="card-img" data-toggle="modal" href="#view-modal-{{post.id}}">
                    <!--<a class="card-img" href="/{{ category }}/view/{{ post.id }}">-->
                        {% if post.image_ext: %}
                            <img src="{{ post.image_ext }}" />
                        {% else %}
                            <img src="{{ url_for('static', filename='images/test-photo.png') }}" />
                        {% endif %}
                    </a>
                    <div class="card-content">
                        <a class="card-subject ellipsis" data-toggle="modal" href="#view-modal-{{post.id}}">
                            {{ post.subject }}
                        </a>
                        <!--<a href="/{{ category }}/view/{{ post.id }}">{{ post.subject }}</a>-->
                        <p class="card-desc ellipsis">
                            <span class="card-desc-price">{{ '${:,}'.format(post.price) }}</span
                            ><span class="card-desc-2"></span>
                        </p>
                        <div class="card-read-more">
                            <p class="card-read-more-text" style="float:left;"><i class="fa fa-map-marker" aria-hidden="true"></i> {{ post.city }}</p>
                            <p class="card-read-more-text" style="float:right;">{{ (today.date()-post.date_posted.date()).days }}일전</p>
                        </div>
                    </div>
                </div><!-- END class card -->
            </div><!-- END grid -->
        );
    }
};

export default HomePostInfo;
